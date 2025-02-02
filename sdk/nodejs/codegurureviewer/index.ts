// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { GetRepositoryAssociationArgs, GetRepositoryAssociationResult, GetRepositoryAssociationOutputArgs } from "./getRepositoryAssociation";
export const getRepositoryAssociation: typeof import("./getRepositoryAssociation").getRepositoryAssociation = null as any;
export const getRepositoryAssociationOutput: typeof import("./getRepositoryAssociation").getRepositoryAssociationOutput = null as any;
utilities.lazyLoad(exports, ["getRepositoryAssociation","getRepositoryAssociationOutput"], () => require("./getRepositoryAssociation"));

export { RepositoryAssociationArgs } from "./repositoryAssociation";
export type RepositoryAssociation = import("./repositoryAssociation").RepositoryAssociation;
export const RepositoryAssociation: typeof import("./repositoryAssociation").RepositoryAssociation = null as any;
utilities.lazyLoad(exports, ["RepositoryAssociation"], () => require("./repositoryAssociation"));


// Export enums:
export * from "../types/enums/codegurureviewer";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:codegurureviewer:RepositoryAssociation":
                return new RepositoryAssociation(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "codegurureviewer", _module)
