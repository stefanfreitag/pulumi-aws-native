// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Schema for AWS::ServiceCatalogAppRegistry::AttributeGroup.
 */
export function getAttributeGroup(args: GetAttributeGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetAttributeGroupResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:servicecatalogappregistry:getAttributeGroup", {
        "id": args.id,
    }, opts);
}

export interface GetAttributeGroupArgs {
    id: string;
}

export interface GetAttributeGroupResult {
    readonly arn?: string;
    readonly attributes?: any;
    /**
     * The description of the attribute group. 
     */
    readonly description?: string;
    readonly id?: string;
    /**
     * The name of the attribute group. 
     */
    readonly name?: string;
    readonly tags?: outputs.servicecatalogappregistry.AttributeGroupTags;
}
/**
 * Resource Schema for AWS::ServiceCatalogAppRegistry::AttributeGroup.
 */
export function getAttributeGroupOutput(args: GetAttributeGroupOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetAttributeGroupResult> {
    return pulumi.output(args).apply((a: any) => getAttributeGroup(a, opts))
}

export interface GetAttributeGroupOutputArgs {
    id: pulumi.Input<string>;
}
