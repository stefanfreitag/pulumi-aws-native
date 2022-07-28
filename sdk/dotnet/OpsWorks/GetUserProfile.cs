// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.OpsWorks
{
    public static class GetUserProfile
    {
        /// <summary>
        /// Resource Type definition for AWS::OpsWorks::UserProfile
        /// </summary>
        public static Task<GetUserProfileResult> InvokeAsync(GetUserProfileArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetUserProfileResult>("aws-native:opsworks:getUserProfile", args ?? new GetUserProfileArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::OpsWorks::UserProfile
        /// </summary>
        public static Output<GetUserProfileResult> Invoke(GetUserProfileInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetUserProfileResult>("aws-native:opsworks:getUserProfile", args ?? new GetUserProfileInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetUserProfileArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetUserProfileArgs()
        {
        }
        public static new GetUserProfileArgs Empty => new GetUserProfileArgs();
    }

    public sealed class GetUserProfileInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetUserProfileInvokeArgs()
        {
        }
        public static new GetUserProfileInvokeArgs Empty => new GetUserProfileInvokeArgs();
    }


    [OutputType]
    public sealed class GetUserProfileResult
    {
        public readonly bool? AllowSelfManagement;
        public readonly string? Id;
        public readonly string? SshPublicKey;
        public readonly string? SshUsername;

        [OutputConstructor]
        private GetUserProfileResult(
            bool? allowSelfManagement,

            string? id,

            string? sshPublicKey,

            string? sshUsername)
        {
            AllowSelfManagement = allowSelfManagement;
            Id = id;
            SshPublicKey = sshPublicKey;
            SshUsername = sshUsername;
        }
    }
}
