// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Pinpoint::PushTemplate
 */
export function getPushTemplate(args: GetPushTemplateArgs, opts?: pulumi.InvokeOptions): Promise<GetPushTemplateResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:pinpoint:getPushTemplate", {
        "id": args.id,
    }, opts);
}

export interface GetPushTemplateArgs {
    id: string;
}

export interface GetPushTemplateResult {
    readonly adm?: outputs.pinpoint.PushTemplateAndroidPushNotificationTemplate;
    readonly apns?: outputs.pinpoint.PushTemplateApnsPushNotificationTemplate;
    readonly arn?: string;
    readonly baidu?: outputs.pinpoint.PushTemplateAndroidPushNotificationTemplate;
    readonly default?: outputs.pinpoint.PushTemplateDefaultPushNotificationTemplate;
    readonly defaultSubstitutions?: string;
    readonly gcm?: outputs.pinpoint.PushTemplateAndroidPushNotificationTemplate;
    readonly id?: string;
    /**
     * Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Pinpoint::PushTemplate` for more information about the expected schema for this property.
     */
    readonly tags?: any;
    readonly templateDescription?: string;
}
/**
 * Resource Type definition for AWS::Pinpoint::PushTemplate
 */
export function getPushTemplateOutput(args: GetPushTemplateOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetPushTemplateResult> {
    return pulumi.output(args).apply((a: any) => getPushTemplate(a, opts))
}

export interface GetPushTemplateOutputArgs {
    id: pulumi.Input<string>;
}
