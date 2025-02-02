// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { DbClusterArgs } from "./dbCluster";
export type DbCluster = import("./dbCluster").DbCluster;
export const DbCluster: typeof import("./dbCluster").DbCluster = null as any;
utilities.lazyLoad(exports, ["DbCluster"], () => require("./dbCluster"));

export { DbClusterParameterGroupArgs } from "./dbClusterParameterGroup";
export type DbClusterParameterGroup = import("./dbClusterParameterGroup").DbClusterParameterGroup;
export const DbClusterParameterGroup: typeof import("./dbClusterParameterGroup").DbClusterParameterGroup = null as any;
utilities.lazyLoad(exports, ["DbClusterParameterGroup"], () => require("./dbClusterParameterGroup"));

export { DbInstanceArgs } from "./dbInstance";
export type DbInstance = import("./dbInstance").DbInstance;
export const DbInstance: typeof import("./dbInstance").DbInstance = null as any;
utilities.lazyLoad(exports, ["DbInstance"], () => require("./dbInstance"));

export { DbSubnetGroupArgs } from "./dbSubnetGroup";
export type DbSubnetGroup = import("./dbSubnetGroup").DbSubnetGroup;
export const DbSubnetGroup: typeof import("./dbSubnetGroup").DbSubnetGroup = null as any;
utilities.lazyLoad(exports, ["DbSubnetGroup"], () => require("./dbSubnetGroup"));

export { EventSubscriptionArgs } from "./eventSubscription";
export type EventSubscription = import("./eventSubscription").EventSubscription;
export const EventSubscription: typeof import("./eventSubscription").EventSubscription = null as any;
utilities.lazyLoad(exports, ["EventSubscription"], () => require("./eventSubscription"));

export { GetDbClusterArgs, GetDbClusterResult, GetDbClusterOutputArgs } from "./getDbCluster";
export const getDbCluster: typeof import("./getDbCluster").getDbCluster = null as any;
export const getDbClusterOutput: typeof import("./getDbCluster").getDbClusterOutput = null as any;
utilities.lazyLoad(exports, ["getDbCluster","getDbClusterOutput"], () => require("./getDbCluster"));

export { GetDbClusterParameterGroupArgs, GetDbClusterParameterGroupResult, GetDbClusterParameterGroupOutputArgs } from "./getDbClusterParameterGroup";
export const getDbClusterParameterGroup: typeof import("./getDbClusterParameterGroup").getDbClusterParameterGroup = null as any;
export const getDbClusterParameterGroupOutput: typeof import("./getDbClusterParameterGroup").getDbClusterParameterGroupOutput = null as any;
utilities.lazyLoad(exports, ["getDbClusterParameterGroup","getDbClusterParameterGroupOutput"], () => require("./getDbClusterParameterGroup"));

export { GetDbInstanceArgs, GetDbInstanceResult, GetDbInstanceOutputArgs } from "./getDbInstance";
export const getDbInstance: typeof import("./getDbInstance").getDbInstance = null as any;
export const getDbInstanceOutput: typeof import("./getDbInstance").getDbInstanceOutput = null as any;
utilities.lazyLoad(exports, ["getDbInstance","getDbInstanceOutput"], () => require("./getDbInstance"));

export { GetDbSubnetGroupArgs, GetDbSubnetGroupResult, GetDbSubnetGroupOutputArgs } from "./getDbSubnetGroup";
export const getDbSubnetGroup: typeof import("./getDbSubnetGroup").getDbSubnetGroup = null as any;
export const getDbSubnetGroupOutput: typeof import("./getDbSubnetGroup").getDbSubnetGroupOutput = null as any;
utilities.lazyLoad(exports, ["getDbSubnetGroup","getDbSubnetGroupOutput"], () => require("./getDbSubnetGroup"));

export { GetEventSubscriptionArgs, GetEventSubscriptionResult, GetEventSubscriptionOutputArgs } from "./getEventSubscription";
export const getEventSubscription: typeof import("./getEventSubscription").getEventSubscription = null as any;
export const getEventSubscriptionOutput: typeof import("./getEventSubscription").getEventSubscriptionOutput = null as any;
utilities.lazyLoad(exports, ["getEventSubscription","getEventSubscriptionOutput"], () => require("./getEventSubscription"));


const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:docdb:DbCluster":
                return new DbCluster(name, <any>undefined, { urn })
            case "aws-native:docdb:DbClusterParameterGroup":
                return new DbClusterParameterGroup(name, <any>undefined, { urn })
            case "aws-native:docdb:DbInstance":
                return new DbInstance(name, <any>undefined, { urn })
            case "aws-native:docdb:DbSubnetGroup":
                return new DbSubnetGroup(name, <any>undefined, { urn })
            case "aws-native:docdb:EventSubscription":
                return new EventSubscription(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "docdb", _module)
