import { createBrowserRouter } from "react-router";
import Login from "~/pages/Login";
import Blackboard from "~/pages/Blackboard";


const router = createBrowserRouter([
  {
    path: "/",
    Component: Login
  },
  {
    path: "/blackboard",
    Component: Blackboard
  }
]);

export default router;