// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./studio";
export * from "./studioSessionMapping";

// Export enums:
export * from "../types/enums/emr";

// Import resources to register:
import { Studio } from "./studio";
import { StudioSessionMapping } from "./studioSessionMapping";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:emr:Studio":
                return new Studio(name, <any>undefined, { urn })
            case "aws-native:emr:StudioSessionMapping":
                return new StudioSessionMapping(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "emr", _module)
