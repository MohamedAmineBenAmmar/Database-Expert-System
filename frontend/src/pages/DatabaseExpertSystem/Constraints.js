import React from "react";
import { Button } from 'primereact/button'
import { InputText } from 'primereact/inputtext'
import { Checkbox } from 'primereact/checkbox'

export default function Constraints() {
  return (
    <div className="flex align-items-center justify-content-center p-4">
      <div className="surface-card p-4 shadow-8 border-round w-full lg:w-6">
        <div className="text-center mb-5">
          <img
            src="assets/images/hyper.svg"
            alt="hyper"
            height={50}
            className="mb-3"
          />
          <div className="text-900 text-3xl font-medium mb-3">Set the requirements of your project</div>
          <span className="text-600 font-medium line-height-3">
            By clicking on run engine our system will provide you with the best databases to use that suits your project
          </span>         
        </div>

        <div>
          <label htmlFor="email" className="block text-900 font-medium mb-2">
            Email
          </label>
          <InputText
            id="email"
            type="text"
            placeholder="Email address"
            className="w-full mb-3"
          />

          <label htmlFor="password" className="block text-900 font-medium mb-2">
            Password
          </label>
          <InputText
            id="password"
            type="password"
            placeholder="Password"
            className="w-full mb-3"
          />

          <div className="flex align-items-center justify-content-between mb-6">
            <div className="flex align-items-center">
              <Checkbox
                id="rememberme"
                // onChange={(e) => setChecked(e.checked)}
                // checked={checked}
                className="mr-2"
              />
              <label htmlFor="rememberme">Remember me</label>
            </div>
            <a className="font-medium no-underline ml-2 text-blue-500 text-right cursor-pointer">
              Forgot your password?
            </a>
          </div>

          <Button label="Run Engine" icon="pi pi-sync" className="w-full" />
        </div>
      </div>
    </div>
  );
}
