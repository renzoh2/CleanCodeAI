import type { Route } from "./+types/Login";
import { type ChangeEvent, useState } from "react";
import { useNavigate, useLoaderData } from "react-router";

//Apollo Client
import { useMutation } from "@apollo/client/react";

//Apollo Queries
import { LOGIN_ACCOUNT } from "~/apollo/auth.queries";

//Import Assets
import Google from "../assets/img/google.png";

export function meta({}: Route.MetaArgs){
    return [
        {
            title: "Clean Code AI"
        },
        {
            name: "description",
            content: "Landing page for Clean Code AI - Login",
        }
    ]
}

type AuthForm = {
    email: string | undefined;
    password: string | undefined;
};

const Login = () => {
    const [email, setEmail] = useState<string | undefined>();
    const [password, setPassword] = useState<string | undefined>();
    const [status, setStatus] = useState<string>("");
    const navigate = useNavigate();

    const [opLogin, {loading}] = useMutation(LOGIN_ACCOUNT);
    const sleep = (ms: number) => new Promise(resolve => setTimeout(resolve, ms));

    const handlesubmit = async (e: ChangeEvent<HTMLFormElement>) => {
        e.preventDefault();
        
        const auth: AuthForm = {
            email,
            password
        }

        //Login Credentials
        const response = await opLogin({
            variables: auth
        })

        const code = response.data?.login?.code;

        if(code != "LOGIN_SUCCESS"){
            setStatus(response.data?.login?.message);
            return;
        }
        
        setStatus("");
        await sleep(3000); 
        navigate("/blackboard");
   
    }

    const onChangeEmail = (e: ChangeEvent<HTMLInputElement>) => {
        setEmail(e.target.value);
    }

    const onChangePassword = (e: ChangeEvent<HTMLInputElement>) => {
        setPassword(e.target.value);
    }

    return (
        <>
        <div className="flex flex-row h-screen">
            <div className="flex-row w-130 p-10">
                <div className="my-10">
                    <span className="font-bold text-2xl">
                        Clean Code <span className="text-palette-red">AI</span>
                    </span>
                </div>
                <div className="grid gap-5 border-2 my-20 border-palette-gray rounded-xl p-5">
                    <form className="grid gap-5" onSubmit={handlesubmit}>
                            <fieldset className="grid border rounded-lg border-gray-500">
                                <input className="outline-none px-2 py-3 rounded-lg bg-white text-palette-dark" type="text" id="login_email" name="login_email" placeholder="Email Address" onChange={onChangeEmail} />
                            </fieldset>
                            <fieldset className="grid border rounded-lg border-gray-500">
                                <input className="outline-none px-2 py-3 rounded-lg bg-white text-palette-dark" type="password" id="login_password" name="login_password" placeholder="Password" onChange={onChangePassword} />
                            </fieldset>
                            <input className="font-bold bg-palette-red text-white rounded-full py-3 w-full" type="submit" value="Sign in your account" />
                    </form>
                    <button disabled={loading} className="font-bold border rounded-full py-2 w-full flex flex-row place-content-center gap-3 p-2 hover:cursor-pointer bg-white text-palette-dark">
                    <img src={Google} className="w-1/10" /><span className="place-content-center">Continue with Google</span>
                    </button>
                    {status && <p>{status}</p>}
                </div>    
                
            </div>
            <div className="flex-row grow">
                <p>Write less bugs.<br />Ship with confidence.<br />Test everything.</p>
            </div>
            
        </div>
        </>
    )
}

export default Login;