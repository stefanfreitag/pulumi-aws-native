// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { CollaborationArgs } from "./collaboration";
export type Collaboration = import("./collaboration").Collaboration;
export const Collaboration: typeof import("./collaboration").Collaboration = null as any;
utilities.lazyLoad(exports, ["Collaboration"], () => require("./collaboration"));

export { ConfiguredTableArgs } from "./configuredTable";
export type ConfiguredTable = import("./configuredTable").ConfiguredTable;
export const ConfiguredTable: typeof import("./configuredTable").ConfiguredTable = null as any;
utilities.lazyLoad(exports, ["ConfiguredTable"], () => require("./configuredTable"));

export { ConfiguredTableAssociationArgs } from "./configuredTableAssociation";
export type ConfiguredTableAssociation = import("./configuredTableAssociation").ConfiguredTableAssociation;
export const ConfiguredTableAssociation: typeof import("./configuredTableAssociation").ConfiguredTableAssociation = null as any;
utilities.lazyLoad(exports, ["ConfiguredTableAssociation"], () => require("./configuredTableAssociation"));

export { GetCollaborationArgs, GetCollaborationResult, GetCollaborationOutputArgs } from "./getCollaboration";
export const getCollaboration: typeof import("./getCollaboration").getCollaboration = null as any;
export const getCollaborationOutput: typeof import("./getCollaboration").getCollaborationOutput = null as any;
utilities.lazyLoad(exports, ["getCollaboration","getCollaborationOutput"], () => require("./getCollaboration"));

export { GetConfiguredTableArgs, GetConfiguredTableResult, GetConfiguredTableOutputArgs } from "./getConfiguredTable";
export const getConfiguredTable: typeof import("./getConfiguredTable").getConfiguredTable = null as any;
export const getConfiguredTableOutput: typeof import("./getConfiguredTable").getConfiguredTableOutput = null as any;
utilities.lazyLoad(exports, ["getConfiguredTable","getConfiguredTableOutput"], () => require("./getConfiguredTable"));

export { GetConfiguredTableAssociationArgs, GetConfiguredTableAssociationResult, GetConfiguredTableAssociationOutputArgs } from "./getConfiguredTableAssociation";
export const getConfiguredTableAssociation: typeof import("./getConfiguredTableAssociation").getConfiguredTableAssociation = null as any;
export const getConfiguredTableAssociationOutput: typeof import("./getConfiguredTableAssociation").getConfiguredTableAssociationOutput = null as any;
utilities.lazyLoad(exports, ["getConfiguredTableAssociation","getConfiguredTableAssociationOutput"], () => require("./getConfiguredTableAssociation"));

export { GetMembershipArgs, GetMembershipResult, GetMembershipOutputArgs } from "./getMembership";
export const getMembership: typeof import("./getMembership").getMembership = null as any;
export const getMembershipOutput: typeof import("./getMembership").getMembershipOutput = null as any;
utilities.lazyLoad(exports, ["getMembership","getMembershipOutput"], () => require("./getMembership"));

export { MembershipArgs } from "./membership";
export type Membership = import("./membership").Membership;
export const Membership: typeof import("./membership").Membership = null as any;
utilities.lazyLoad(exports, ["Membership"], () => require("./membership"));


// Export enums:
export * from "../types/enums/cleanrooms";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:cleanrooms:Collaboration":
                return new Collaboration(name, <any>undefined, { urn })
            case "aws-native:cleanrooms:ConfiguredTable":
                return new ConfiguredTable(name, <any>undefined, { urn })
            case "aws-native:cleanrooms:ConfiguredTableAssociation":
                return new ConfiguredTableAssociation(name, <any>undefined, { urn })
            case "aws-native:cleanrooms:Membership":
                return new Membership(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "cleanrooms", _module)
