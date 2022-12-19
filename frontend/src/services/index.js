import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000/",
});

export const getSuggestions = (reqBody) => {
  return new Promise((resolve, reject) => {
    try {
      api
        .post("/suggest_databases", reqBody)
        .then((res) => {
          console.log("axios res=", res);
          resolve(res.data);
        })
        .catch((err) => {
          console.log("Get Suggestions Error=", err);
          reject("GET_SUGGESTIONS_ERROR");
        });
    } catch (error) {
      console.error("Get Suggestions Erro=", error);
      reject("GET_SUGGESTIONS_ERROR");
    }
  });
};
