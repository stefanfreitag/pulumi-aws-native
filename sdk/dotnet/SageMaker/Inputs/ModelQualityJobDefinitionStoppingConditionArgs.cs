// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Inputs
{

    /// <summary>
    /// Specifies a time limit for how long the monitoring job is allowed to run.
    /// </summary>
    public sealed class ModelQualityJobDefinitionStoppingConditionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The maximum runtime allowed in seconds.
        /// </summary>
        [Input("maxRuntimeInSeconds", required: true)]
        public Input<int> MaxRuntimeInSeconds { get; set; } = null!;

        public ModelQualityJobDefinitionStoppingConditionArgs()
        {
        }
        public static new ModelQualityJobDefinitionStoppingConditionArgs Empty => new ModelQualityJobDefinitionStoppingConditionArgs();
    }
}
