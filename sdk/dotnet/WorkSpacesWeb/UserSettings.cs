// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WorkSpacesWeb
{
    /// <summary>
    /// Definition of AWS::WorkSpacesWeb::UserSettings Resource Type
    /// </summary>
    [AwsNativeResourceType("aws-native:workspacesweb:UserSettings")]
    public partial class UserSettings : global::Pulumi.CustomResource
    {
        [Output("additionalEncryptionContext")]
        public Output<Outputs.UserSettingsEncryptionContextMap?> AdditionalEncryptionContext { get; private set; } = null!;

        [Output("associatedPortalArns")]
        public Output<ImmutableArray<string>> AssociatedPortalArns { get; private set; } = null!;

        [Output("cookieSynchronizationConfiguration")]
        public Output<Outputs.UserSettingsCookieSynchronizationConfiguration?> CookieSynchronizationConfiguration { get; private set; } = null!;

        [Output("copyAllowed")]
        public Output<Pulumi.AwsNative.WorkSpacesWeb.UserSettingsEnabledType> CopyAllowed { get; private set; } = null!;

        [Output("customerManagedKey")]
        public Output<string?> CustomerManagedKey { get; private set; } = null!;

        [Output("disconnectTimeoutInMinutes")]
        public Output<double?> DisconnectTimeoutInMinutes { get; private set; } = null!;

        [Output("downloadAllowed")]
        public Output<Pulumi.AwsNative.WorkSpacesWeb.UserSettingsEnabledType> DownloadAllowed { get; private set; } = null!;

        [Output("idleDisconnectTimeoutInMinutes")]
        public Output<double?> IdleDisconnectTimeoutInMinutes { get; private set; } = null!;

        [Output("pasteAllowed")]
        public Output<Pulumi.AwsNative.WorkSpacesWeb.UserSettingsEnabledType> PasteAllowed { get; private set; } = null!;

        [Output("printAllowed")]
        public Output<Pulumi.AwsNative.WorkSpacesWeb.UserSettingsEnabledType> PrintAllowed { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.UserSettingsTag>> Tags { get; private set; } = null!;

        [Output("uploadAllowed")]
        public Output<Pulumi.AwsNative.WorkSpacesWeb.UserSettingsEnabledType> UploadAllowed { get; private set; } = null!;

        [Output("userSettingsArn")]
        public Output<string> UserSettingsArn { get; private set; } = null!;


        /// <summary>
        /// Create a UserSettings resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public UserSettings(string name, UserSettingsArgs args, CustomResourceOptions? options = null)
            : base("aws-native:workspacesweb:UserSettings", name, args ?? new UserSettingsArgs(), MakeResourceOptions(options, ""))
        {
        }

        private UserSettings(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:workspacesweb:UserSettings", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "additionalEncryptionContext",
                    "customerManagedKey",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing UserSettings resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static UserSettings Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new UserSettings(name, id, options);
        }
    }

    public sealed class UserSettingsArgs : global::Pulumi.ResourceArgs
    {
        [Input("additionalEncryptionContext")]
        public Input<Inputs.UserSettingsEncryptionContextMapArgs>? AdditionalEncryptionContext { get; set; }

        [Input("cookieSynchronizationConfiguration")]
        public Input<Inputs.UserSettingsCookieSynchronizationConfigurationArgs>? CookieSynchronizationConfiguration { get; set; }

        [Input("copyAllowed", required: true)]
        public Input<Pulumi.AwsNative.WorkSpacesWeb.UserSettingsEnabledType> CopyAllowed { get; set; } = null!;

        [Input("customerManagedKey")]
        public Input<string>? CustomerManagedKey { get; set; }

        [Input("disconnectTimeoutInMinutes")]
        public Input<double>? DisconnectTimeoutInMinutes { get; set; }

        [Input("downloadAllowed", required: true)]
        public Input<Pulumi.AwsNative.WorkSpacesWeb.UserSettingsEnabledType> DownloadAllowed { get; set; } = null!;

        [Input("idleDisconnectTimeoutInMinutes")]
        public Input<double>? IdleDisconnectTimeoutInMinutes { get; set; }

        [Input("pasteAllowed", required: true)]
        public Input<Pulumi.AwsNative.WorkSpacesWeb.UserSettingsEnabledType> PasteAllowed { get; set; } = null!;

        [Input("printAllowed", required: true)]
        public Input<Pulumi.AwsNative.WorkSpacesWeb.UserSettingsEnabledType> PrintAllowed { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.UserSettingsTagArgs>? _tags;
        public InputList<Inputs.UserSettingsTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.UserSettingsTagArgs>());
            set => _tags = value;
        }

        [Input("uploadAllowed", required: true)]
        public Input<Pulumi.AwsNative.WorkSpacesWeb.UserSettingsEnabledType> UploadAllowed { get; set; } = null!;

        public UserSettingsArgs()
        {
        }
        public static new UserSettingsArgs Empty => new UserSettingsArgs();
    }
}
