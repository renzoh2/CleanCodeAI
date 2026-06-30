import { type RouteConfig, index, route } from "@react-router/dev/routes";

export default [
    index("pages/Login.tsx"),
    route("/blackboard", "pages/Blackboard.tsx")
] satisfies RouteConfig;
