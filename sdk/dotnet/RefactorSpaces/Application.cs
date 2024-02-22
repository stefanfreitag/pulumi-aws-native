// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.RefactorSpaces
{
    /// <summary>
    /// Definition of AWS::RefactorSpaces::Application Resource Type
    /// </summary>
    [AwsNativeResourceType("aws-native:refactorspaces:Application")]
    public partial class Application : global::Pulumi.CustomResource
    {
        [Output("apiGatewayId")]
        public Output<string> ApiGatewayId { get; private set; } = null!;

        [Output("apiGatewayProxy")]
        public Output<Outputs.ApplicationApiGatewayProxyInput?> ApiGatewayProxy { get; private set; } = null!;

        [Output("applicationIdentifier")]
        public Output<string> ApplicationIdentifier { get; private set; } = null!;

        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("environmentIdentifier")]
        public Output<string> EnvironmentIdentifier { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("nlbArn")]
        public Output<string> NlbArn { get; private set; } = null!;

        [Output("nlbName")]
        public Output<string> NlbName { get; private set; } = null!;

        [Output("proxyType")]
        public Output<Pulumi.AwsNative.RefactorSpaces.ApplicationProxyType> ProxyType { get; private set; } = null!;

        [Output("proxyUrl")]
        public Output<string> ProxyUrl { get; private set; } = null!;

        [Output("stageName")]
        public Output<string> StageName { get; private set; } = null!;

        /// <summary>
        /// Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;

        [Output("vpcId")]
        public Output<string> VpcId { get; private set; } = null!;

        [Output("vpcLinkId")]
        public Output<string> VpcLinkId { get; private set; } = null!;


        /// <summary>
        /// Create a Application resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Application(string name, ApplicationArgs args, CustomResourceOptions? options = null)
            : base("aws-native:refactorspaces:Application", name, args ?? new ApplicationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Application(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:refactorspaces:Application", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "apiGatewayProxy",
                    "environmentIdentifier",
                    "name",
                    "proxyType",
                    "vpcId",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Application resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Application Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Application(name, id, options);
        }
    }

    public sealed class ApplicationArgs : global::Pulumi.ResourceArgs
    {
        [Input("apiGatewayProxy")]
        public Input<Inputs.ApplicationApiGatewayProxyInputArgs>? ApiGatewayProxy { get; set; }

        [Input("environmentIdentifier", required: true)]
        public Input<string> EnvironmentIdentifier { get; set; } = null!;

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("proxyType", required: true)]
        public Input<Pulumi.AwsNative.RefactorSpaces.ApplicationProxyType> ProxyType { get; set; } = null!;

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        [Input("vpcId", required: true)]
        public Input<string> VpcId { get; set; } = null!;

        public ApplicationArgs()
        {
        }
        public static new ApplicationArgs Empty => new ApplicationArgs();
    }
}
