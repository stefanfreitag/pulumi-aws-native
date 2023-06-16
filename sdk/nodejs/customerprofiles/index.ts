// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { CalculatedAttributeDefinitionArgs } from "./calculatedAttributeDefinition";
export type CalculatedAttributeDefinition = import("./calculatedAttributeDefinition").CalculatedAttributeDefinition;
export const CalculatedAttributeDefinition: typeof import("./calculatedAttributeDefinition").CalculatedAttributeDefinition = null as any;
utilities.lazyLoad(exports, ["CalculatedAttributeDefinition"], () => require("./calculatedAttributeDefinition"));

export { DomainArgs } from "./domain";
export type Domain = import("./domain").Domain;
export const Domain: typeof import("./domain").Domain = null as any;
utilities.lazyLoad(exports, ["Domain"], () => require("./domain"));

export { EventStreamArgs } from "./eventStream";
export type EventStream = import("./eventStream").EventStream;
export const EventStream: typeof import("./eventStream").EventStream = null as any;
utilities.lazyLoad(exports, ["EventStream"], () => require("./eventStream"));

export { GetCalculatedAttributeDefinitionArgs, GetCalculatedAttributeDefinitionResult, GetCalculatedAttributeDefinitionOutputArgs } from "./getCalculatedAttributeDefinition";
export const getCalculatedAttributeDefinition: typeof import("./getCalculatedAttributeDefinition").getCalculatedAttributeDefinition = null as any;
export const getCalculatedAttributeDefinitionOutput: typeof import("./getCalculatedAttributeDefinition").getCalculatedAttributeDefinitionOutput = null as any;
utilities.lazyLoad(exports, ["getCalculatedAttributeDefinition","getCalculatedAttributeDefinitionOutput"], () => require("./getCalculatedAttributeDefinition"));

export { GetDomainArgs, GetDomainResult, GetDomainOutputArgs } from "./getDomain";
export const getDomain: typeof import("./getDomain").getDomain = null as any;
export const getDomainOutput: typeof import("./getDomain").getDomainOutput = null as any;
utilities.lazyLoad(exports, ["getDomain","getDomainOutput"], () => require("./getDomain"));

export { GetEventStreamArgs, GetEventStreamResult, GetEventStreamOutputArgs } from "./getEventStream";
export const getEventStream: typeof import("./getEventStream").getEventStream = null as any;
export const getEventStreamOutput: typeof import("./getEventStream").getEventStreamOutput = null as any;
utilities.lazyLoad(exports, ["getEventStream","getEventStreamOutput"], () => require("./getEventStream"));

export { GetIntegrationArgs, GetIntegrationResult, GetIntegrationOutputArgs } from "./getIntegration";
export const getIntegration: typeof import("./getIntegration").getIntegration = null as any;
export const getIntegrationOutput: typeof import("./getIntegration").getIntegrationOutput = null as any;
utilities.lazyLoad(exports, ["getIntegration","getIntegrationOutput"], () => require("./getIntegration"));

export { GetObjectTypeArgs, GetObjectTypeResult, GetObjectTypeOutputArgs } from "./getObjectType";
export const getObjectType: typeof import("./getObjectType").getObjectType = null as any;
export const getObjectTypeOutput: typeof import("./getObjectType").getObjectTypeOutput = null as any;
utilities.lazyLoad(exports, ["getObjectType","getObjectTypeOutput"], () => require("./getObjectType"));

export { IntegrationArgs } from "./integration";
export type Integration = import("./integration").Integration;
export const Integration: typeof import("./integration").Integration = null as any;
utilities.lazyLoad(exports, ["Integration"], () => require("./integration"));

export { ObjectTypeArgs } from "./objectType";
export type ObjectType = import("./objectType").ObjectType;
export const ObjectType: typeof import("./objectType").ObjectType = null as any;
utilities.lazyLoad(exports, ["ObjectType"], () => require("./objectType"));


// Export enums:
export * from "../types/enums/customerprofiles";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:customerprofiles:CalculatedAttributeDefinition":
                return new CalculatedAttributeDefinition(name, <any>undefined, { urn })
            case "aws-native:customerprofiles:Domain":
                return new Domain(name, <any>undefined, { urn })
            case "aws-native:customerprofiles:EventStream":
                return new EventStream(name, <any>undefined, { urn })
            case "aws-native:customerprofiles:Integration":
                return new Integration(name, <any>undefined, { urn })
            case "aws-native:customerprofiles:ObjectType":
                return new ObjectType(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "customerprofiles", _module)
