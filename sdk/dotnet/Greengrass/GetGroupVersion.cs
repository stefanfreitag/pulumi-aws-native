// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Greengrass
{
    public static class GetGroupVersion
    {
        /// <summary>
        /// Resource Type definition for AWS::Greengrass::GroupVersion
        /// </summary>
        public static Task<GetGroupVersionResult> InvokeAsync(GetGroupVersionArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetGroupVersionResult>("aws-native:greengrass:getGroupVersion", args ?? new GetGroupVersionArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Greengrass::GroupVersion
        /// </summary>
        public static Output<GetGroupVersionResult> Invoke(GetGroupVersionInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetGroupVersionResult>("aws-native:greengrass:getGroupVersion", args ?? new GetGroupVersionInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetGroupVersionArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetGroupVersionArgs()
        {
        }
        public static new GetGroupVersionArgs Empty => new GetGroupVersionArgs();
    }

    public sealed class GetGroupVersionInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetGroupVersionInvokeArgs()
        {
        }
        public static new GetGroupVersionInvokeArgs Empty => new GetGroupVersionInvokeArgs();
    }


    [OutputType]
    public sealed class GetGroupVersionResult
    {
        public readonly string? Id;

        [OutputConstructor]
        private GetGroupVersionResult(string? id)
        {
            Id = id;
        }
    }
}
