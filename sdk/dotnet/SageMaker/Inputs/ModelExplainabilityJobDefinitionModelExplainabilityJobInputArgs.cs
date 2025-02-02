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
    /// The inputs for a monitoring job.
    /// </summary>
    public sealed class ModelExplainabilityJobDefinitionModelExplainabilityJobInputArgs : global::Pulumi.ResourceArgs
    {
        [Input("batchTransformInput")]
        public Input<Inputs.ModelExplainabilityJobDefinitionBatchTransformInputArgs>? BatchTransformInput { get; set; }

        [Input("endpointInput")]
        public Input<Inputs.ModelExplainabilityJobDefinitionEndpointInputArgs>? EndpointInput { get; set; }

        public ModelExplainabilityJobDefinitionModelExplainabilityJobInputArgs()
        {
        }
        public static new ModelExplainabilityJobDefinitionModelExplainabilityJobInputArgs Empty => new ModelExplainabilityJobDefinitionModelExplainabilityJobInputArgs();
    }
}
