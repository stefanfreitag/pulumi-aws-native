// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./registry";
export * from "./schema";
export * from "./schemaVersion";
export * from "./schemaVersionMetadata";

// Export enums:
export * from "../types/enums/glue";

// Import resources to register:
import { Registry } from "./registry";
import { Schema } from "./schema";
import { SchemaVersion } from "./schemaVersion";
import { SchemaVersionMetadata } from "./schemaVersionMetadata";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:glue:Registry":
                return new Registry(name, <any>undefined, { urn })
            case "aws-native:glue:Schema":
                return new Schema(name, <any>undefined, { urn })
            case "aws-native:glue:SchemaVersion":
                return new SchemaVersion(name, <any>undefined, { urn })
            case "aws-native:glue:SchemaVersionMetadata":
                return new SchemaVersionMetadata(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "glue", _module)
