// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::SES::VdmAttributes
 */
export function getVdmAttributes(args: GetVdmAttributesArgs, opts?: pulumi.InvokeOptions): Promise<GetVdmAttributesResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:ses:getVdmAttributes", {
        "vdmAttributesResourceId": args.vdmAttributesResourceId,
    }, opts);
}

export interface GetVdmAttributesArgs {
    /**
     * Unique identifier for this resource
     */
    vdmAttributesResourceId: string;
}

export interface GetVdmAttributesResult {
    readonly dashboardAttributes?: outputs.ses.VdmAttributesDashboardAttributes;
    readonly guardianAttributes?: outputs.ses.VdmAttributesGuardianAttributes;
    /**
     * Unique identifier for this resource
     */
    readonly vdmAttributesResourceId?: string;
}
/**
 * Resource Type definition for AWS::SES::VdmAttributes
 */
export function getVdmAttributesOutput(args: GetVdmAttributesOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetVdmAttributesResult> {
    return pulumi.output(args).apply((a: any) => getVdmAttributes(a, opts))
}

export interface GetVdmAttributesOutputArgs {
    /**
     * Unique identifier for this resource
     */
    vdmAttributesResourceId: pulumi.Input<string>;
}
