import { type RouteConfig, route } from "@react-router/dev/routes";

export default [
    route("/", "pages/login.tsx"),
    route("/blackboard", "pages/blackboard.tsx")
] satisfies RouteConfig;
