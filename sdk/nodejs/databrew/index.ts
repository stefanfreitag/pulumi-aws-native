// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./dataset";
export * from "./job";
export * from "./project";
export * from "./recipe";
export * from "./schedule";

// Export enums:
export * from "../types/enums/databrew";

// Import resources to register:
import { Dataset } from "./dataset";
import { Job } from "./job";
import { Project } from "./project";
import { Recipe } from "./recipe";
import { Schedule } from "./schedule";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:databrew:Dataset":
                return new Dataset(name, <any>undefined, { urn })
            case "aws-native:databrew:Job":
                return new Job(name, <any>undefined, { urn })
            case "aws-native:databrew:Project":
                return new Project(name, <any>undefined, { urn })
            case "aws-native:databrew:Recipe":
                return new Recipe(name, <any>undefined, { urn })
            case "aws-native:databrew:Schedule":
                return new Schedule(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "databrew", _module)
