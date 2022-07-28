// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lambda.Inputs
{

    /// <summary>
    /// The function's AWS X-Ray tracing configuration. To sample and record incoming requests, set Mode to Active.
    /// </summary>
    public sealed class FunctionTracingConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The tracing mode.
        /// </summary>
        [Input("mode")]
        public Input<Pulumi.AwsNative.Lambda.FunctionTracingConfigMode>? Mode { get; set; }

        public FunctionTracingConfigArgs()
        {
        }
        public static new FunctionTracingConfigArgs Empty => new FunctionTracingConfigArgs();
    }
}
