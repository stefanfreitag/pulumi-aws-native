// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./alias";
export * from "./fleet";
export * from "./gameServerGroup";

// Export enums:
export * from "../types/enums/gamelift";

// Import resources to register:
import { Alias } from "./alias";
import { Fleet } from "./fleet";
import { GameServerGroup } from "./gameServerGroup";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:gamelift:Alias":
                return new Alias(name, <any>undefined, { urn })
            case "aws-native:gamelift:Fleet":
                return new Fleet(name, <any>undefined, { urn })
            case "aws-native:gamelift:GameServerGroup":
                return new GameServerGroup(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "gamelift", _module)
