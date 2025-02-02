// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ServiceCatalog::PortfolioProductAssociation
 */
export function getPortfolioProductAssociation(args: GetPortfolioProductAssociationArgs, opts?: pulumi.InvokeOptions): Promise<GetPortfolioProductAssociationResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:servicecatalog:getPortfolioProductAssociation", {
        "id": args.id,
    }, opts);
}

export interface GetPortfolioProductAssociationArgs {
    id: string;
}

export interface GetPortfolioProductAssociationResult {
    readonly id?: string;
}
/**
 * Resource Type definition for AWS::ServiceCatalog::PortfolioProductAssociation
 */
export function getPortfolioProductAssociationOutput(args: GetPortfolioProductAssociationOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetPortfolioProductAssociationResult> {
    return pulumi.output(args).apply((a: any) => getPortfolioProductAssociation(a, opts))
}

export interface GetPortfolioProductAssociationOutputArgs {
    id: pulumi.Input<string>;
}
