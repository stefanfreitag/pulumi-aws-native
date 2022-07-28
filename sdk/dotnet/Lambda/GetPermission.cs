// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lambda
{
    public static class GetPermission
    {
        /// <summary>
        /// Resource Type definition for AWS::Lambda::Permission
        /// </summary>
        public static Task<GetPermissionResult> InvokeAsync(GetPermissionArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetPermissionResult>("aws-native:lambda:getPermission", args ?? new GetPermissionArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Lambda::Permission
        /// </summary>
        public static Output<GetPermissionResult> Invoke(GetPermissionInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetPermissionResult>("aws-native:lambda:getPermission", args ?? new GetPermissionInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPermissionArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetPermissionArgs()
        {
        }
        public static new GetPermissionArgs Empty => new GetPermissionArgs();
    }

    public sealed class GetPermissionInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetPermissionInvokeArgs()
        {
        }
        public static new GetPermissionInvokeArgs Empty => new GetPermissionInvokeArgs();
    }


    [OutputType]
    public sealed class GetPermissionResult
    {
        public readonly string? Id;

        [OutputConstructor]
        private GetPermissionResult(string? id)
        {
            Id = id;
        }
    }
}
