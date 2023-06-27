// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppStream
{
    /// <summary>
    /// Resource Type definition for AWS::AppStream::Stack
    /// </summary>
    [Obsolete(@"Stack is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:appstream:Stack")]
    public partial class Stack : global::Pulumi.CustomResource
    {
        [Output("accessEndpoints")]
        public Output<ImmutableArray<Outputs.StackAccessEndpoint>> AccessEndpoints { get; private set; } = null!;

        [Output("applicationSettings")]
        public Output<Outputs.StackApplicationSettings?> ApplicationSettings { get; private set; } = null!;

        [Output("attributesToDelete")]
        public Output<ImmutableArray<string>> AttributesToDelete { get; private set; } = null!;

        [Output("deleteStorageConnectors")]
        public Output<bool?> DeleteStorageConnectors { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("displayName")]
        public Output<string?> DisplayName { get; private set; } = null!;

        [Output("embedHostDomains")]
        public Output<ImmutableArray<string>> EmbedHostDomains { get; private set; } = null!;

        [Output("feedbackURL")]
        public Output<string?> FeedbackURL { get; private set; } = null!;

        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        [Output("redirectURL")]
        public Output<string?> RedirectURL { get; private set; } = null!;

        [Output("storageConnectors")]
        public Output<ImmutableArray<Outputs.StackStorageConnector>> StorageConnectors { get; private set; } = null!;

        [Output("streamingExperienceSettings")]
        public Output<Outputs.StackStreamingExperienceSettings?> StreamingExperienceSettings { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.StackTag>> Tags { get; private set; } = null!;

        [Output("userSettings")]
        public Output<ImmutableArray<Outputs.StackUserSetting>> UserSettings { get; private set; } = null!;


        /// <summary>
        /// Create a Stack resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Stack(string name, StackArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:appstream:Stack", name, args ?? new StackArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Stack(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:appstream:Stack", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Stack resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Stack Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Stack(name, id, options);
        }
    }

    public sealed class StackArgs : global::Pulumi.ResourceArgs
    {
        [Input("accessEndpoints")]
        private InputList<Inputs.StackAccessEndpointArgs>? _accessEndpoints;
        public InputList<Inputs.StackAccessEndpointArgs> AccessEndpoints
        {
            get => _accessEndpoints ?? (_accessEndpoints = new InputList<Inputs.StackAccessEndpointArgs>());
            set => _accessEndpoints = value;
        }

        [Input("applicationSettings")]
        public Input<Inputs.StackApplicationSettingsArgs>? ApplicationSettings { get; set; }

        [Input("attributesToDelete")]
        private InputList<string>? _attributesToDelete;
        public InputList<string> AttributesToDelete
        {
            get => _attributesToDelete ?? (_attributesToDelete = new InputList<string>());
            set => _attributesToDelete = value;
        }

        [Input("deleteStorageConnectors")]
        public Input<bool>? DeleteStorageConnectors { get; set; }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        [Input("embedHostDomains")]
        private InputList<string>? _embedHostDomains;
        public InputList<string> EmbedHostDomains
        {
            get => _embedHostDomains ?? (_embedHostDomains = new InputList<string>());
            set => _embedHostDomains = value;
        }

        [Input("feedbackURL")]
        public Input<string>? FeedbackURL { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("redirectURL")]
        public Input<string>? RedirectURL { get; set; }

        [Input("storageConnectors")]
        private InputList<Inputs.StackStorageConnectorArgs>? _storageConnectors;
        public InputList<Inputs.StackStorageConnectorArgs> StorageConnectors
        {
            get => _storageConnectors ?? (_storageConnectors = new InputList<Inputs.StackStorageConnectorArgs>());
            set => _storageConnectors = value;
        }

        [Input("streamingExperienceSettings")]
        public Input<Inputs.StackStreamingExperienceSettingsArgs>? StreamingExperienceSettings { get; set; }

        [Input("tags")]
        private InputList<Inputs.StackTagArgs>? _tags;
        public InputList<Inputs.StackTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.StackTagArgs>());
            set => _tags = value;
        }

        [Input("userSettings")]
        private InputList<Inputs.StackUserSettingArgs>? _userSettings;
        public InputList<Inputs.StackUserSettingArgs> UserSettings
        {
            get => _userSettings ?? (_userSettings = new InputList<Inputs.StackUserSettingArgs>());
            set => _userSettings = value;
        }

        public StackArgs()
        {
        }
        public static new StackArgs Empty => new StackArgs();
    }
}
