import { HttpLink, InMemoryCache } from "@apollo/client";
import {
  createApolloLoaderHandler,
  ApolloClient,
} from "@apollo/client-integration-react-router";


const baseUrl = {
    graphql: import.meta.env.VITE_BASE_BACKEND_FULL_URL+"/app/"
}


// `request` will be available on the server during SSR or in loaders, but not in the browser
export const makeClient = (request?: Request) => {
  return new ApolloClient({
    cache: new InMemoryCache(),
    link: new HttpLink({uri: baseUrl.graphql }),
  });
};
export const apolloLoader = createApolloLoaderHandler(makeClient);