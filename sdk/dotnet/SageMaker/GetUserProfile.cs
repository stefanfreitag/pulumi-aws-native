// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker
{
    public static class GetUserProfile
    {
        /// <summary>
        /// Resource Type definition for AWS::SageMaker::UserProfile
        /// </summary>
        public static Task<GetUserProfileResult> InvokeAsync(GetUserProfileArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetUserProfileResult>("aws-native:sagemaker:getUserProfile", args ?? new GetUserProfileArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::SageMaker::UserProfile
        /// </summary>
        public static Output<GetUserProfileResult> Invoke(GetUserProfileInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetUserProfileResult>("aws-native:sagemaker:getUserProfile", args ?? new GetUserProfileInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetUserProfileArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the associated Domain.
        /// </summary>
        [Input("domainId", required: true)]
        public string DomainId { get; set; } = null!;

        /// <summary>
        /// A name for the UserProfile.
        /// </summary>
        [Input("userProfileName", required: true)]
        public string UserProfileName { get; set; } = null!;

        public GetUserProfileArgs()
        {
        }
        public static new GetUserProfileArgs Empty => new GetUserProfileArgs();
    }

    public sealed class GetUserProfileInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the associated Domain.
        /// </summary>
        [Input("domainId", required: true)]
        public Input<string> DomainId { get; set; } = null!;

        /// <summary>
        /// A name for the UserProfile.
        /// </summary>
        [Input("userProfileName", required: true)]
        public Input<string> UserProfileName { get; set; } = null!;

        public GetUserProfileInvokeArgs()
        {
        }
        public static new GetUserProfileInvokeArgs Empty => new GetUserProfileInvokeArgs();
    }


    [OutputType]
    public sealed class GetUserProfileResult
    {
        /// <summary>
        /// The user profile Amazon Resource Name (ARN).
        /// </summary>
        public readonly string? UserProfileArn;
        /// <summary>
        /// A collection of settings.
        /// </summary>
        public readonly Outputs.UserProfileUserSettings? UserSettings;

        [OutputConstructor]
        private GetUserProfileResult(
            string? userProfileArn,

            Outputs.UserProfileUserSettings? userSettings)
        {
            UserProfileArn = userProfileArn;
            UserSettings = userSettings;
        }
    }
}
