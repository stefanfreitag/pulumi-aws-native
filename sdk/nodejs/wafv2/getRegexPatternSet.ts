// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Contains a list of Regular expressions based on the provided inputs. RegexPatternSet can be used with other WAF entities with RegexPatternSetReferenceStatement to perform other actions .
 */
export function getRegexPatternSet(args: GetRegexPatternSetArgs, opts?: pulumi.InvokeOptions): Promise<GetRegexPatternSetResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:wafv2:getRegexPatternSet", {
        "id": args.id,
        "name": args.name,
        "scope": args.scope,
    }, opts);
}

export interface GetRegexPatternSetArgs {
    /**
     * Id of the RegexPatternSet
     */
    id: string;
    /**
     * Name of the RegexPatternSet.
     */
    name: string;
    /**
     * Use CLOUDFRONT for CloudFront RegexPatternSet, use REGIONAL for Application Load Balancer and API Gateway.
     */
    scope: enums.wafv2.RegexPatternSetScope;
}

export interface GetRegexPatternSetResult {
    /**
     * ARN of the WAF entity.
     */
    readonly arn?: string;
    /**
     * Description of the entity.
     */
    readonly description?: string;
    /**
     * Id of the RegexPatternSet
     */
    readonly id?: string;
    readonly regularExpressionList?: string[];
    readonly tags?: outputs.Tag[];
}
/**
 * Contains a list of Regular expressions based on the provided inputs. RegexPatternSet can be used with other WAF entities with RegexPatternSetReferenceStatement to perform other actions .
 */
export function getRegexPatternSetOutput(args: GetRegexPatternSetOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetRegexPatternSetResult> {
    return pulumi.output(args).apply((a: any) => getRegexPatternSet(a, opts))
}

export interface GetRegexPatternSetOutputArgs {
    /**
     * Id of the RegexPatternSet
     */
    id: pulumi.Input<string>;
    /**
     * Name of the RegexPatternSet.
     */
    name: pulumi.Input<string>;
    /**
     * Use CLOUDFRONT for CloudFront RegexPatternSet, use REGIONAL for Application Load Balancer and API Gateway.
     */
    scope: pulumi.Input<enums.wafv2.RegexPatternSetScope>;
}
