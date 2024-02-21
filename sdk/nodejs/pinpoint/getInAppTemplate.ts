// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Pinpoint::InAppTemplate
 */
export function getInAppTemplate(args: GetInAppTemplateArgs, opts?: pulumi.InvokeOptions): Promise<GetInAppTemplateResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:pinpoint:getInAppTemplate", {
        "templateName": args.templateName,
    }, opts);
}

export interface GetInAppTemplateArgs {
    templateName: string;
}

export interface GetInAppTemplateResult {
    readonly arn?: string;
    readonly content?: outputs.pinpoint.InAppTemplateInAppMessageContent[];
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Pinpoint::InAppTemplate` for more information about the expected schema for this property.
     */
    readonly customConfig?: any;
    readonly layout?: enums.pinpoint.InAppTemplateLayout;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Pinpoint::InAppTemplate` for more information about the expected schema for this property.
     */
    readonly tags?: any;
    readonly templateDescription?: string;
}
/**
 * Resource Type definition for AWS::Pinpoint::InAppTemplate
 */
export function getInAppTemplateOutput(args: GetInAppTemplateOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetInAppTemplateResult> {
    return pulumi.output(args).apply((a: any) => getInAppTemplate(a, opts))
}

export interface GetInAppTemplateOutputArgs {
    templateName: pulumi.Input<string>;
}
