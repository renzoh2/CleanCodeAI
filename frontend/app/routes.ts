import { type RouteConfig, index, route } from "@react-router/dev/routes";

export default [
    index("pages/login.tsx"),
    route("/blackboard", "pages/blackboard.tsx")
] satisfies RouteConfig;
