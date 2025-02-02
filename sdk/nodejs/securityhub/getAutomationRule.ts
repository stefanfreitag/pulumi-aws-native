// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The ``AWS::SecurityHub::AutomationRule`` resource specifies an automation rule based on input parameters. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *User Guide*.
 */
export function getAutomationRule(args: GetAutomationRuleArgs, opts?: pulumi.InvokeOptions): Promise<GetAutomationRuleResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:securityhub:getAutomationRule", {
        "ruleArn": args.ruleArn,
    }, opts);
}

export interface GetAutomationRuleArgs {
    ruleArn: string;
}

export interface GetAutomationRuleResult {
    readonly actions?: outputs.securityhub.AutomationRulesAction[];
    readonly createdAt?: string;
    readonly createdBy?: string;
    /**
     * A set of [Security Finding Format (ASFF)](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html) finding field attributes and corresponding expected values that ASH uses to filter findings. If a rule is enabled and a finding matches the criteria specified in this parameter, ASH applies the rule action to the finding.
     */
    readonly criteria?: outputs.securityhub.AutomationRulesFindingFilters;
    readonly description?: string;
    readonly isTerminal?: boolean;
    readonly ruleArn?: string;
    readonly ruleName?: string;
    readonly ruleOrder?: number;
    /**
     * Whether the rule is active after it is created. If this parameter is equal to ``ENABLED``, ASH applies the rule to findings and finding updates after the rule is created.
     */
    readonly ruleStatus?: enums.securityhub.AutomationRuleRuleStatus;
    readonly tags?: {[key: string]: string};
    readonly updatedAt?: string;
}
/**
 * The ``AWS::SecurityHub::AutomationRule`` resource specifies an automation rule based on input parameters. For more information, see [Automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *User Guide*.
 */
export function getAutomationRuleOutput(args: GetAutomationRuleOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetAutomationRuleResult> {
    return pulumi.output(args).apply((a: any) => getAutomationRule(a, opts))
}

export interface GetAutomationRuleOutputArgs {
    ruleArn: pulumi.Input<string>;
}
