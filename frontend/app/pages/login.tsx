import type { Route } from "./+types/login";
import { useState } from "react";

export function meta({}: Route.MetaArgs){
    return [
        {
            title: "Clean Code AI"
        },
        {
            name: "description",
            content: "Still a project",
        }
    ]
}

function login() {

    const [username, setUsername] = useState<string | undefined>();
    const [password, setPassword] = useState<string | undefined>();

    async function handlesubmit(e: React.ChangeEvent<HTMLFormElement>){
        e.preventDefault();
        console.log("trigger")
        console.log(username)
        console.log(password)
    }

    async function onChangeUsername(e: React.ChangeEvent<HTMLInputElement>){
        setUsername(e.target.value)
    }

    async function onChangePassword(e: React.ChangeEvent<HTMLInputElement>){
        setPassword(e.target.value)
    }

    return (
        <>
            <div className="bg-white text-black content-center width-20">
                <h3>Login Account</h3>
                <form onSubmit={handlesubmit}>
                    <fieldset>
                        <label htmlFor="login_username">Username/Email</label>
                        <input id="login_username" type="text" name="login_username" onChange={onChangeUsername} />
                        <br />
                        <label htmlFor="login_password">Password</label>
                        <input id="login_password" type="password" name="login_password" onChange={onChangePassword} />
                        <br />
                        <input type="submit" value="Login" />
                    </fieldset>
                </form>
            </div>
        </>
    )
}

export default login