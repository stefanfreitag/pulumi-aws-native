// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::DataSync::LocationFSxONTAP.
 */
export class LocationFSxOntap extends pulumi.CustomResource {
    /**
     * Get an existing LocationFSxOntap resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): LocationFSxOntap {
        return new LocationFSxOntap(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:datasync:LocationFSxOntap';

    /**
     * Returns true if the given object is an instance of LocationFSxOntap.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is LocationFSxOntap {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === LocationFSxOntap.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN) for the FSx ONAP file system.
     */
    public /*out*/ readonly fsxFilesystemArn!: pulumi.Output<string>;
    /**
     * The Amazon Resource Name (ARN) of the Amazon FSx ONTAP file system location that is created.
     */
    public /*out*/ readonly locationArn!: pulumi.Output<string>;
    /**
     * The URL of the FSx ONTAP file system that was described.
     */
    public /*out*/ readonly locationUri!: pulumi.Output<string>;
    public readonly protocol!: pulumi.Output<outputs.datasync.LocationFSxOntapProtocol | undefined>;
    /**
     * The ARNs of the security groups that are to use to configure the FSx ONTAP file system.
     */
    public readonly securityGroupArns!: pulumi.Output<string[]>;
    /**
     * The Amazon Resource Name (ARN) for the FSx ONTAP SVM.
     */
    public readonly storageVirtualMachineArn!: pulumi.Output<string>;
    /**
     * A subdirectory in the location's path.
     */
    public readonly subdirectory!: pulumi.Output<string | undefined>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a LocationFSxOntap resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: LocationFSxOntapArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.securityGroupArns === undefined) && !opts.urn) {
                throw new Error("Missing required property 'securityGroupArns'");
            }
            if ((!args || args.storageVirtualMachineArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'storageVirtualMachineArn'");
            }
            resourceInputs["protocol"] = args ? args.protocol : undefined;
            resourceInputs["securityGroupArns"] = args ? args.securityGroupArns : undefined;
            resourceInputs["storageVirtualMachineArn"] = args ? args.storageVirtualMachineArn : undefined;
            resourceInputs["subdirectory"] = args ? args.subdirectory : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["fsxFilesystemArn"] = undefined /*out*/;
            resourceInputs["locationArn"] = undefined /*out*/;
            resourceInputs["locationUri"] = undefined /*out*/;
        } else {
            resourceInputs["fsxFilesystemArn"] = undefined /*out*/;
            resourceInputs["locationArn"] = undefined /*out*/;
            resourceInputs["locationUri"] = undefined /*out*/;
            resourceInputs["protocol"] = undefined /*out*/;
            resourceInputs["securityGroupArns"] = undefined /*out*/;
            resourceInputs["storageVirtualMachineArn"] = undefined /*out*/;
            resourceInputs["subdirectory"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["protocol", "securityGroupArns[*]", "storageVirtualMachineArn", "subdirectory"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(LocationFSxOntap.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a LocationFSxOntap resource.
 */
export interface LocationFSxOntapArgs {
    protocol?: pulumi.Input<inputs.datasync.LocationFSxOntapProtocolArgs>;
    /**
     * The ARNs of the security groups that are to use to configure the FSx ONTAP file system.
     */
    securityGroupArns: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The Amazon Resource Name (ARN) for the FSx ONTAP SVM.
     */
    storageVirtualMachineArn: pulumi.Input<string>;
    /**
     * A subdirectory in the location's path.
     */
    subdirectory?: pulumi.Input<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
