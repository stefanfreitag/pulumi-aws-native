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
    public sealed class AutomationRuleNoteUpdate
    {
        public readonly string Text;
        public readonly Outputs.AutomationRulearnOrId UpdatedBy;

        [OutputConstructor]
        private AutomationRuleNoteUpdate(
            string text,

            Outputs.AutomationRulearnOrId updatedBy)
        {
            Text = text;
            UpdatedBy = updatedBy;
        }
    }
}
