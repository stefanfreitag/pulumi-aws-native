// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Outputs
{

    [OutputType]
    public sealed class AnalysisCustomActionURLOperation
    {
        public readonly Pulumi.AwsNative.QuickSight.AnalysisURLTargetConfiguration URLTarget;
        public readonly string URLTemplate;

        [OutputConstructor]
        private AnalysisCustomActionURLOperation(
            Pulumi.AwsNative.QuickSight.AnalysisURLTargetConfiguration uRLTarget,

            string uRLTemplate)
        {
            URLTarget = uRLTarget;
            URLTemplate = uRLTemplate;
        }
    }
}
