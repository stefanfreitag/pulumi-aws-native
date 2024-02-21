// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SecurityHub.Outputs
{

    /// <summary>
    /// Provides details about a list of findings that the current finding relates to.
    /// </summary>
    [OutputType]
    public sealed class AutomationRuleRelatedFinding
    {
        public readonly string Id;
        /// <summary>
        /// The Amazon Resource Name (ARN) for the product that generated a related finding.
        /// </summary>
        public readonly string ProductArn;

        [OutputConstructor]
        private AutomationRuleRelatedFinding(
            string id,

            string productArn)
        {
            Id = id;
            ProductArn = productArn;
        }
    }
}
