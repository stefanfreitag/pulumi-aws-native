// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SecurityHub.Outputs
{

    [OutputType]
    public sealed class AutomationRulesAction
    {
        public readonly Outputs.AutomationRulesFindingFieldsUpdate FindingFieldsUpdate;
        public readonly Pulumi.AwsNative.SecurityHub.AutomationRulesActionType Type;

        [OutputConstructor]
        private AutomationRulesAction(
            Outputs.AutomationRulesFindingFieldsUpdate findingFieldsUpdate,

            Pulumi.AwsNative.SecurityHub.AutomationRulesActionType type)
        {
            FindingFieldsUpdate = findingFieldsUpdate;
            Type = type;
        }
    }
}
