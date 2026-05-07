import { type TypedDocumentNode, gql } from "@apollo/client";

export const LOGIN_ACCOUNT: TypedDocumentNode =  gql`
    mutation Login($email: String, $password: String) {
        login(email:$email, password:$password) {
            code
            message
        }
    }
` 