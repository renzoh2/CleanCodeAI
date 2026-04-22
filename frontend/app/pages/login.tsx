import type { Route } from "./+types/login";

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
    return (
        <>
            <div className="bg-white text-black content-center width-20">
                <h3>Login Account</h3>
                <form>
                    <fieldset>
                        <label htmlFor="username">Username/Email</label>
                        <input type="text" name="login_username" />
                        <br />
                        <label htmlFor="password">Password</label>
                        <input type="password" name="login_password" />
                        <br />
                        <input type="submit" value="Login" />
                    </fieldset>
                </form>
            </div>
        </>
    )
}

export default login