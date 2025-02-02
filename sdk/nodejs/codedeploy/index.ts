// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { ApplicationArgs } from "./application";
export type Application = import("./application").Application;
export const Application: typeof import("./application").Application = null as any;
utilities.lazyLoad(exports, ["Application"], () => require("./application"));

export { DeploymentConfigArgs } from "./deploymentConfig";
export type DeploymentConfig = import("./deploymentConfig").DeploymentConfig;
export const DeploymentConfig: typeof import("./deploymentConfig").DeploymentConfig = null as any;
utilities.lazyLoad(exports, ["DeploymentConfig"], () => require("./deploymentConfig"));

export { DeploymentGroupArgs } from "./deploymentGroup";
export type DeploymentGroup = import("./deploymentGroup").DeploymentGroup;
export const DeploymentGroup: typeof import("./deploymentGroup").DeploymentGroup = null as any;
utilities.lazyLoad(exports, ["DeploymentGroup"], () => require("./deploymentGroup"));

export { GetApplicationArgs, GetApplicationResult, GetApplicationOutputArgs } from "./getApplication";
export const getApplication: typeof import("./getApplication").getApplication = null as any;
export const getApplicationOutput: typeof import("./getApplication").getApplicationOutput = null as any;
utilities.lazyLoad(exports, ["getApplication","getApplicationOutput"], () => require("./getApplication"));

export { GetDeploymentGroupArgs, GetDeploymentGroupResult, GetDeploymentGroupOutputArgs } from "./getDeploymentGroup";
export const getDeploymentGroup: typeof import("./getDeploymentGroup").getDeploymentGroup = null as any;
export const getDeploymentGroupOutput: typeof import("./getDeploymentGroup").getDeploymentGroupOutput = null as any;
utilities.lazyLoad(exports, ["getDeploymentGroup","getDeploymentGroupOutput"], () => require("./getDeploymentGroup"));


const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:codedeploy:Application":
                return new Application(name, <any>undefined, { urn })
            case "aws-native:codedeploy:DeploymentConfig":
                return new DeploymentConfig(name, <any>undefined, { urn })
            case "aws-native:codedeploy:DeploymentGroup":
                return new DeploymentGroup(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "codedeploy", _module)
