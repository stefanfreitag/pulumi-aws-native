// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EFS::AccessPoint
 */
export class AccessPoint extends pulumi.CustomResource {
    /**
     * Get an existing AccessPoint resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): AccessPoint {
        return new AccessPoint(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:efs:AccessPoint';

    /**
     * Returns true if the given object is an instance of AccessPoint.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AccessPoint {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AccessPoint.__pulumiType;
    }

    public /*out*/ readonly accessPointId!: pulumi.Output<string>;
    public readonly accessPointTags!: pulumi.Output<outputs.efs.AccessPointTag[] | undefined>;
    public /*out*/ readonly arn!: pulumi.Output<string>;
    /**
     * (optional) A string of up to 64 ASCII characters that Amazon EFS uses to ensure idempotent creation.
     */
    public readonly clientToken!: pulumi.Output<string | undefined>;
    /**
     * The ID of the EFS file system that the access point provides access to.
     */
    public readonly fileSystemId!: pulumi.Output<string>;
    /**
     * The operating system user and group applied to all file system requests made using the access point.
     */
    public readonly posixUser!: pulumi.Output<outputs.efs.AccessPointPosixUser | undefined>;
    /**
     * Specifies the directory on the Amazon EFS file system that the access point exposes as the root directory of your file system to NFS clients using the access point. The clients using the access point can only access the root directory and below. If the RootDirectory>Path specified does not exist, EFS creates it and applies the CreationInfo settings when a client connects to an access point. When specifying a RootDirectory, you need to provide the Path, and the CreationInfo is optional.
     */
    public readonly rootDirectory!: pulumi.Output<outputs.efs.AccessPointRootDirectory | undefined>;

    /**
     * Create a AccessPoint resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AccessPointArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.fileSystemId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'fileSystemId'");
            }
            resourceInputs["accessPointTags"] = args ? args.accessPointTags : undefined;
            resourceInputs["clientToken"] = args ? args.clientToken : undefined;
            resourceInputs["fileSystemId"] = args ? args.fileSystemId : undefined;
            resourceInputs["posixUser"] = args ? args.posixUser : undefined;
            resourceInputs["rootDirectory"] = args ? args.rootDirectory : undefined;
            resourceInputs["accessPointId"] = undefined /*out*/;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["accessPointId"] = undefined /*out*/;
            resourceInputs["accessPointTags"] = undefined /*out*/;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["clientToken"] = undefined /*out*/;
            resourceInputs["fileSystemId"] = undefined /*out*/;
            resourceInputs["posixUser"] = undefined /*out*/;
            resourceInputs["rootDirectory"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(AccessPoint.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a AccessPoint resource.
 */
export interface AccessPointArgs {
    accessPointTags?: pulumi.Input<pulumi.Input<inputs.efs.AccessPointTagArgs>[]>;
    /**
     * (optional) A string of up to 64 ASCII characters that Amazon EFS uses to ensure idempotent creation.
     */
    clientToken?: pulumi.Input<string>;
    /**
     * The ID of the EFS file system that the access point provides access to.
     */
    fileSystemId: pulumi.Input<string>;
    /**
     * The operating system user and group applied to all file system requests made using the access point.
     */
    posixUser?: pulumi.Input<inputs.efs.AccessPointPosixUserArgs>;
    /**
     * Specifies the directory on the Amazon EFS file system that the access point exposes as the root directory of your file system to NFS clients using the access point. The clients using the access point can only access the root directory and below. If the RootDirectory>Path specified does not exist, EFS creates it and applies the CreationInfo settings when a client connects to an access point. When specifying a RootDirectory, you need to provide the Path, and the CreationInfo is optional.
     */
    rootDirectory?: pulumi.Input<inputs.efs.AccessPointRootDirectoryArgs>;
}
