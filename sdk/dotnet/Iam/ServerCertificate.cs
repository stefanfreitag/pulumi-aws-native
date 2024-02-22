// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Iam
{
    /// <summary>
    /// Resource Type definition for AWS::IAM::ServerCertificate
    /// </summary>
    [AwsNativeResourceType("aws-native:iam:ServerCertificate")]
    public partial class ServerCertificate : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Amazon Resource Name (ARN) of the server certificate
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("certificateBody")]
        public Output<string?> CertificateBody { get; private set; } = null!;

        [Output("certificateChain")]
        public Output<string?> CertificateChain { get; private set; } = null!;

        [Output("path")]
        public Output<string?> Path { get; private set; } = null!;

        [Output("privateKey")]
        public Output<string?> PrivateKey { get; private set; } = null!;

        [Output("serverCertificateName")]
        public Output<string?> ServerCertificateName { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a ServerCertificate resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ServerCertificate(string name, ServerCertificateArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:iam:ServerCertificate", name, args ?? new ServerCertificateArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ServerCertificate(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:iam:ServerCertificate", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "certificateBody",
                    "certificateChain",
                    "privateKey",
                    "serverCertificateName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ServerCertificate resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ServerCertificate Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ServerCertificate(name, id, options);
        }
    }

    public sealed class ServerCertificateArgs : global::Pulumi.ResourceArgs
    {
        [Input("certificateBody")]
        public Input<string>? CertificateBody { get; set; }

        [Input("certificateChain")]
        public Input<string>? CertificateChain { get; set; }

        [Input("path")]
        public Input<string>? Path { get; set; }

        [Input("privateKey")]
        public Input<string>? PrivateKey { get; set; }

        [Input("serverCertificateName")]
        public Input<string>? ServerCertificateName { get; set; }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        public ServerCertificateArgs()
        {
        }
        public static new ServerCertificateArgs Empty => new ServerCertificateArgs();
    }
}
