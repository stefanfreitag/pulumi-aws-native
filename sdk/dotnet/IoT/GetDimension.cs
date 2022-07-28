// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoT
{
    public static class GetDimension
    {
        /// <summary>
        /// A dimension can be used to limit the scope of a metric used in a security profile for AWS IoT Device Defender.
        /// </summary>
        public static Task<GetDimensionResult> InvokeAsync(GetDimensionArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetDimensionResult>("aws-native:iot:getDimension", args ?? new GetDimensionArgs(), options.WithDefaults());

        /// <summary>
        /// A dimension can be used to limit the scope of a metric used in a security profile for AWS IoT Device Defender.
        /// </summary>
        public static Output<GetDimensionResult> Invoke(GetDimensionInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetDimensionResult>("aws-native:iot:getDimension", args ?? new GetDimensionInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDimensionArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// A unique identifier for the dimension.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetDimensionArgs()
        {
        }
        public static new GetDimensionArgs Empty => new GetDimensionArgs();
    }

    public sealed class GetDimensionInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// A unique identifier for the dimension.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetDimensionInvokeArgs()
        {
        }
        public static new GetDimensionInvokeArgs Empty => new GetDimensionInvokeArgs();
    }


    [OutputType]
    public sealed class GetDimensionResult
    {
        /// <summary>
        /// The ARN (Amazon resource name) of the created dimension.
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// Specifies the value or list of values for the dimension.
        /// </summary>
        public readonly ImmutableArray<string> StringValues;
        /// <summary>
        /// Metadata that can be used to manage the dimension.
        /// </summary>
        public readonly ImmutableArray<Outputs.DimensionTag> Tags;

        [OutputConstructor]
        private GetDimensionResult(
            string? arn,

            ImmutableArray<string> stringValues,

            ImmutableArray<Outputs.DimensionTag> tags)
        {
            Arn = arn;
            StringValues = stringValues;
            Tags = tags;
        }
    }
}
