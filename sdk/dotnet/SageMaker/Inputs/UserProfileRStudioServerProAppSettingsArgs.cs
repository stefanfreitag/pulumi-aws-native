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
    /// A collection of settings that configure user interaction with the RStudioServerPro app.
    /// </summary>
    public sealed class UserProfileRStudioServerProAppSettingsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Indicates whether the current user has access to the RStudioServerPro app.
        /// </summary>
        [Input("accessStatus")]
        public Input<Pulumi.AwsNative.SageMaker.UserProfileRStudioServerProAppSettingsAccessStatus>? AccessStatus { get; set; }

        /// <summary>
        /// The level of permissions that the user has within the RStudioServerPro app. This value defaults to User. The Admin value allows the user access to the RStudio Administrative Dashboard.
        /// </summary>
        [Input("userGroup")]
        public Input<Pulumi.AwsNative.SageMaker.UserProfileRStudioServerProAppSettingsUserGroup>? UserGroup { get; set; }

        public UserProfileRStudioServerProAppSettingsArgs()
        {
        }
        public static new UserProfileRStudioServerProAppSettingsArgs Empty => new UserProfileRStudioServerProAppSettingsArgs();
    }
}
