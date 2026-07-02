import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { RouterProvider } from "react-router/dom";
import { ApolloClient, HttpLink, InMemoryCache } from "@apollo/client";
import { ApolloProvider } from "@apollo/client/react";

import './index.css';
import router from './router.tsx';

const base = import.meta.env.VITE_BASE_BACKEND_FULL_URL;
const alias = import.meta.env.VITE_BACKEND_GRAPHQL_ALIAS

const client = new ApolloClient({
  link: new HttpLink({ uri: base+"/"+alias+"/" }),
  cache: new InMemoryCache(),
});

createRoot(document.getElementById('root')!).render(
  <StrictMode>
     <ApolloProvider client={client}>
        <RouterProvider router={router} />
    </ApolloProvider>
  </StrictMode>,
)
