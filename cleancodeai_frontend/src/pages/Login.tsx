import { useState } from "react";
import { useNavigate } from "react-router";

//Apollo Client
import { useMutation } from "@apollo/client/react";

//Apollo Queries
import { LOGIN_ACCOUNT } from "~/apollo/auth.queries";

//Hook Forms
import { useForm, type SubmitHandler } from "react-hook-form";

//Import Assets
import imgGoogle from "/img/google.png";

type AuthForm = {
    email: string | undefined;
    password: string | undefined;
};

const Login = () => {
    const {register, handleSubmit} = useForm<AuthForm>();

    const [status, setStatus] = useState<string>("");
    const navigate = useNavigate();

    const [opLogin, {loading}] = useMutation(LOGIN_ACCOUNT);
    const sleep = (ms: number) => new Promise(resolve => setTimeout(resolve, ms));

    const loginSubmit: SubmitHandler<AuthForm>  = async (data: AuthForm) => {
        setStatus("");
        //Login Function
        try{ 
            const response = await opLogin({
                variables: data
            })
            const code = response.data?.login?.code;

            if(code != "LOGIN_SUCCESS"){
                setStatus(response.data?.login?.data.message); 
                await sleep(3000); 
                setStatus("");
                return;
            }

            navigate("/blackboard");
        } catch(error: unknown){
            setStatus("System Error. Please come back later.");
            await sleep(3000);
            setStatus("");
        }
    }

    return (
        <>
        <div className="h-screen">
            <div className="flex flex-row h-5/6">
                <div className="flex-row lg:w-3/7 md:w-1/2 pl-10">
                    <div className="h-1/5 p-5 place-content-center">
                        <span className="font-bold text-2xl">
                            Clean Code <span className="text-palette-red">AI</span>
                        </span>
                    </div>
                    <div className="h-2/4 py-3 px-3 place-content-center">
                            <form className="grid gap-7 mx-10 py-15 px-10 border-2 border-palette-gray rounded-2xl" onSubmit={handleSubmit(loginSubmit)}>
                                <div className="grid gap-5">
                                    <fieldset className="grid border rounded-lg border-gray-500">
                                    <input className="outline-none px-2 py-4 rounded-lg bg-white text-palette-dark placeholder:font-bold placeholder:text-xl" type="text" id="login_email" placeholder="Email Address" {...register("email")} />
                                    </fieldset>
                                    <fieldset className="grid border rounded-lg border-gray-500">
                                        <input className="outline-none px-2 py-4 rounded-lg bg-white text-palette-dark placeholder:font-bold placeholder:text-xl" type="password" id="login_password" placeholder="Password" {...register("password")} />
                                    </fieldset>
                                </div>
                                <div className="grid gap-5">
                                    <input className="font-bold bg-palette-red text-white rounded-full py-4 w-full text-lg" type="submit" value="Sign in your account" />
                                    <button disabled={loading} className="font-bold border rounded-full py-4 w-full flex flex-row place-content-center gap-3 p-2 hover:cursor-pointer bg-white text-palette-dark">
                                    <img src={imgGoogle} className="w-1/15" /><span className="place-content-center text-lg">Continue with Google</span>
                                    </button>
                                </div>
                            </form>
                            {status && <p>{status}</p>}
                    </div>  
                </div>
                <div className="flex-row grow place-content-center">
                    <div className="h-1/2 py-5">
                        <p className="text-6xl font-semibold my-5">
                            Write less <span className="text-palette-red">bugs.</span><br />
                            Ship with <span className="text-palette-red">confidence.</span><br />
                            Test <span className="text-palette-red">everything.</span>
                        </p>
                        <p className="my-5">
                            Paste any code below. Get test cases, debug insights, or a full review instantly
                        </p>
                        <div className="flex flex-row gap-3">
                            <div className="bg-palette-gray text-white w-1/4 py-2 rounded-xl text-center">
                                Generate Code
                            </div>
                            <div className="bg-palette-gray text-white w-1/4 py-2 rounded-xl text-center">
                                Debug Errors
                            </div>
                            <div className="bg-palette-gray text-white w-1/4 py-2 rounded-xl text-center">
                                Code Review
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div className="flex flex-col h-1/6">
                <a href="vscode:extension/JetBrains.resharper-code" className="p-5 mx-25 my-5 border-2 border-palette-gray rounded-2xl">
                    <div className="flex flex-col">
                        <p>Want this inside your editor?</p>
                        <p>Connect the VS Code extension - same AI, zero copy-paste, full codebase context.</p>
                    </div>
                    <div className="flex flex-row">
                        
                    </div>
                </a>
            </div>
        </div>
        
        </>
    );
}

export default Login;