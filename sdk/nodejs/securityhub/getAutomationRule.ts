// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::SecurityHub::AutomationRule resource represents the Automation Rule in your account. One rule resource is created for each Automation Rule in which you configure rule criteria and actions.
 */
export function getAutomationRule(args: GetAutomationRuleArgs, opts?: pulumi.InvokeOptions): Promise<GetAutomationRuleResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:securityhub:getAutomationRule", {
        "ruleArn": args.ruleArn,
    }, opts);
}

export interface GetAutomationRuleArgs {
    /**
     * An Automation Rule Arn is automatically created
     */
    ruleArn: string;
}

export interface GetAutomationRuleResult {
    readonly actions?: outputs.securityhub.AutomationRulesAction[];
    /**
     * The date and time when Automation Rule was created
     */
    readonly createdAt?: string;
    /**
     * The identifier by which created the rule
     */
    readonly createdBy?: string;
    /**
     * The rule criteria for evaluating findings
     */
    readonly criteria?: outputs.securityhub.AutomationRulesFindingFilters;
    /**
     * Rule description
     */
    readonly description?: string;
    /**
     * If Rule is a terminal rule
     */
    readonly isTerminal?: boolean;
    /**
     * An Automation Rule Arn is automatically created
     */
    readonly ruleArn?: string;
    /**
     * Rule name
     */
    readonly ruleName?: string;
    /**
     * Rule order value
     */
    readonly ruleOrder?: number;
    /**
     * Status of the Rule upon creation
     */
    readonly ruleStatus?: enums.securityhub.AutomationRuleRuleStatus;
    readonly tags?: outputs.securityhub.AutomationRuleTags;
    /**
     * The date and time when Automation Rule was last updated
     */
    readonly updatedAt?: string;
}
/**
 * The AWS::SecurityHub::AutomationRule resource represents the Automation Rule in your account. One rule resource is created for each Automation Rule in which you configure rule criteria and actions.
 */
export function getAutomationRuleOutput(args: GetAutomationRuleOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetAutomationRuleResult> {
    return pulumi.output(args).apply((a: any) => getAutomationRule(a, opts))
}

export interface GetAutomationRuleOutputArgs {
    /**
     * An Automation Rule Arn is automatically created
     */
    ruleArn: pulumi.Input<string>;
}
