// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Efs
{
    /// <summary>
    /// The ``AWS::EFS::AccessPoint`` resource creates an EFS access point. An access point is an application-specific view into an EFS file system that applies an operating system user and group, and a file system path, to any file system request made through the access point. The operating system user and group override any identity information provided by the NFS client. The file system path is exposed as the access point's root directory. Applications using the access point can only access data in its own directory and below. To learn more, see [Mounting a file system using EFS access points](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html).
    ///  This operation requires permissions for the ``elasticfilesystem:CreateAccessPoint`` action.
    /// </summary>
    [AwsNativeResourceType("aws-native:efs:AccessPoint")]
    public partial class AccessPoint : global::Pulumi.CustomResource
    {
        [Output("accessPointId")]
        public Output<string> AccessPointId { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        ///  For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
        /// </summary>
        [Output("accessPointTags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> AccessPointTags { get; private set; } = null!;

        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The opaque string specified in the request to ensure idempotent creation.
        /// </summary>
        [Output("clientToken")]
        public Output<string?> ClientToken { get; private set; } = null!;

        /// <summary>
        /// The ID of the EFS file system that the access point applies to. Accepts only the ID format for input when specifying a file system, for example ``fs-0123456789abcedf2``.
        /// </summary>
        [Output("fileSystemId")]
        public Output<string> FileSystemId { get; private set; } = null!;

        /// <summary>
        /// The full POSIX identity, including the user ID, group ID, and secondary group IDs on the access point that is used for all file operations by NFS clients using the access point.
        /// </summary>
        [Output("posixUser")]
        public Output<Outputs.AccessPointPosixUser?> PosixUser { get; private set; } = null!;

        /// <summary>
        /// The directory on the EFS file system that the access point exposes as the root directory to NFS clients using the access point.
        /// </summary>
        [Output("rootDirectory")]
        public Output<Outputs.AccessPointRootDirectory?> RootDirectory { get; private set; } = null!;


        /// <summary>
        /// Create a AccessPoint resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AccessPoint(string name, AccessPointArgs args, CustomResourceOptions? options = null)
            : base("aws-native:efs:AccessPoint", name, args ?? new AccessPointArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AccessPoint(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:efs:AccessPoint", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "clientToken",
                    "fileSystemId",
                    "posixUser",
                    "rootDirectory",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing AccessPoint resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AccessPoint Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new AccessPoint(name, id, options);
        }
    }

    public sealed class AccessPointArgs : global::Pulumi.ResourceArgs
    {
        [Input("accessPointTags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _accessPointTags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        ///  For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> AccessPointTags
        {
            get => _accessPointTags ?? (_accessPointTags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _accessPointTags = value;
        }

        /// <summary>
        /// The opaque string specified in the request to ensure idempotent creation.
        /// </summary>
        [Input("clientToken")]
        public Input<string>? ClientToken { get; set; }

        /// <summary>
        /// The ID of the EFS file system that the access point applies to. Accepts only the ID format for input when specifying a file system, for example ``fs-0123456789abcedf2``.
        /// </summary>
        [Input("fileSystemId", required: true)]
        public Input<string> FileSystemId { get; set; } = null!;

        /// <summary>
        /// The full POSIX identity, including the user ID, group ID, and secondary group IDs on the access point that is used for all file operations by NFS clients using the access point.
        /// </summary>
        [Input("posixUser")]
        public Input<Inputs.AccessPointPosixUserArgs>? PosixUser { get; set; }

        /// <summary>
        /// The directory on the EFS file system that the access point exposes as the root directory to NFS clients using the access point.
        /// </summary>
        [Input("rootDirectory")]
        public Input<Inputs.AccessPointRootDirectoryArgs>? RootDirectory { get; set; }

        public AccessPointArgs()
        {
        }
        public static new AccessPointArgs Empty => new AccessPointArgs();
    }
}
