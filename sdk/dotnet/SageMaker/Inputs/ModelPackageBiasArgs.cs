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
    /// Contains bias metrics for a model.
    /// </summary>
    public sealed class ModelPackageBiasArgs : global::Pulumi.ResourceArgs
    {
        [Input("postTrainingReport")]
        public Input<Inputs.ModelPackageMetricsSourceArgs>? PostTrainingReport { get; set; }

        [Input("preTrainingReport")]
        public Input<Inputs.ModelPackageMetricsSourceArgs>? PreTrainingReport { get; set; }

        [Input("report")]
        public Input<Inputs.ModelPackageMetricsSourceArgs>? Report { get; set; }

        public ModelPackageBiasArgs()
        {
        }
        public static new ModelPackageBiasArgs Empty => new ModelPackageBiasArgs();
    }
}
