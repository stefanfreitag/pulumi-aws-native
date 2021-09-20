// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export * from "./detectorModel";
export * from "./input";

// Export enums:
export * from "../types/enums/iotevents";

// Import resources to register:
import { DetectorModel } from "./detectorModel";
import { Input } from "./input";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:iotevents:DetectorModel":
                return new DetectorModel(name, <any>undefined, { urn })
            case "aws-native:iotevents:Input":
                return new Input(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "iotevents", _module)
