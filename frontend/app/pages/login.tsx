import type { Route } from "./+types/Login";
import { type ChangeEvent, useState } from "react";
import { useNavigate } from "react-router";

//Import Assets
import Google from "../assets/img/google.png";

export function meta({}: Route.MetaArgs){
    return [
        {
            title: "Clean Code AI"
        },
        {
            name: "description",
            content: "Landing page for Clean Code AI",
        }
    ]
}

const Login = () => {

    const [email, setEmail] = useState<string | undefined>();
    const [password, setPassword] = useState<string | undefined>();
    const navigate = useNavigate()

    const handlesubmit = (e: ChangeEvent<HTMLFormElement>) => {
        e.preventDefault();
        console.log("trigger");
        console.log(email);
        console.log(password);
        navigate("/Blackboard")
    }

    const onChangeEmail = (e: ChangeEvent<HTMLInputElement>) => {
        setEmail(e.target.value)
    }

    const onChangePassword = (e: ChangeEvent<HTMLInputElement>) => {
        setPassword(e.target.value)
    }

    return (
        <>
        <div className="grid h-screen place-items-center bg-[url(assets/img/background.png)]">
            <div className="grid gap-2 place-items-center p-6 rounded-lg bg-white text-black">
               
                <h3 className="font-bold">Login Your Account</h3>
                
                <form className="grid gap-2" onSubmit={handlesubmit}>
                    <fieldset className="grid gap-2">
                        <fieldset className="grid border rounded-lg border-gray-500 hover:border-black focus:border-black">
                            <label className="font-bold text-xs pt-1 px-1" htmlFor="login_email">Email Address</label>
                            <input className="outline-none px-1 pb-1 autofill:rounded-lg" type="text" id="login_email" name="login_email" onChange={onChangeEmail} />
                        </fieldset>
                        <fieldset className="grid border rounded-lg border-gray-500 hover:border-black focus:border-black">
                             <label className="font-bold text-xs pt-1 px-1" htmlFor="login_password">Password</label>
                              <input className="outline-none px-1 pb-1 autofill:rounded-lg" type="password" id="login_password" name="login_password" onChange={onChangePassword} />
                        </fieldset>
                    </fieldset>
                    <fieldset>
                        <input type="checkbox" id="remember_me"/>
                        <label htmlFor="remember_me"> Remember me</label>
                    </fieldset>
                    <input className="text-sm font-bold bg-blue-800 focus:bg-blue-500 hover:bg-blue-500 text-white rounded-lg py-2" type="submit" value="Continue with Email" />
                </form>
                <button className="text-sm font-bold border rounded-lg py-2 w-full flex flex-row place-content-center gap-2 p-2 hover:cursor-pointer">
                   <img src={Google} className="w-1/10" /><span className="place-content-center">Continue with Google</span>
                </button>
            </div>
        </div>
        </>
    )
}

export default Login;