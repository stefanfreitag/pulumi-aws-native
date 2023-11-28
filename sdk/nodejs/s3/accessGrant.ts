// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::S3::AccessGrant resource is an Amazon S3 resource type representing permissions to a specific S3 bucket or prefix hosted in an S3 Access Grants instance.
 */
export class AccessGrant extends pulumi.CustomResource {
    /**
     * Get an existing AccessGrant resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): AccessGrant {
        return new AccessGrant(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:s3:AccessGrant';

    /**
     * Returns true if the given object is an instance of AccessGrant.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AccessGrant {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AccessGrant.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN) of the specified access grant.
     */
    public /*out*/ readonly accessGrantArn!: pulumi.Output<string>;
    /**
     * The ID assigned to this access grant.
     */
    public /*out*/ readonly accessGrantId!: pulumi.Output<string>;
    /**
     * The configuration options of the grant location, which is the S3 path to the data to which you are granting access.
     */
    public readonly accessGrantsLocationConfiguration!: pulumi.Output<outputs.s3.AccessGrantsLocationConfiguration | undefined>;
    /**
     * The custom S3 location to be accessed by the grantee
     */
    public readonly accessGrantsLocationId!: pulumi.Output<string>;
    /**
     * The ARN of the application grantees will use to access the location
     */
    public readonly applicationArn!: pulumi.Output<string | undefined>;
    /**
     * The S3 path of the data to which you are granting access. It is a combination of the S3 path of the registered location and the subprefix.
     */
    public /*out*/ readonly grantScope!: pulumi.Output<string>;
    /**
     * The principal who will be granted permission to access S3.
     */
    public readonly grantee!: pulumi.Output<outputs.s3.AccessGrantGrantee>;
    /**
     * The level of access to be afforded to the grantee
     */
    public readonly permission!: pulumi.Output<enums.s3.AccessGrantPermission>;
    /**
     * The type of S3SubPrefix.
     */
    public readonly s3PrefixType!: pulumi.Output<enums.s3.AccessGrantS3PrefixType | undefined>;
    public readonly tags!: pulumi.Output<outputs.s3.AccessGrantTag[] | undefined>;

    /**
     * Create a AccessGrant resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AccessGrantArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.accessGrantsLocationId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'accessGrantsLocationId'");
            }
            if ((!args || args.grantee === undefined) && !opts.urn) {
                throw new Error("Missing required property 'grantee'");
            }
            if ((!args || args.permission === undefined) && !opts.urn) {
                throw new Error("Missing required property 'permission'");
            }
            resourceInputs["accessGrantsLocationConfiguration"] = args ? args.accessGrantsLocationConfiguration : undefined;
            resourceInputs["accessGrantsLocationId"] = args ? args.accessGrantsLocationId : undefined;
            resourceInputs["applicationArn"] = args ? args.applicationArn : undefined;
            resourceInputs["grantee"] = args ? args.grantee : undefined;
            resourceInputs["permission"] = args ? args.permission : undefined;
            resourceInputs["s3PrefixType"] = args ? args.s3PrefixType : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["accessGrantArn"] = undefined /*out*/;
            resourceInputs["accessGrantId"] = undefined /*out*/;
            resourceInputs["grantScope"] = undefined /*out*/;
        } else {
            resourceInputs["accessGrantArn"] = undefined /*out*/;
            resourceInputs["accessGrantId"] = undefined /*out*/;
            resourceInputs["accessGrantsLocationConfiguration"] = undefined /*out*/;
            resourceInputs["accessGrantsLocationId"] = undefined /*out*/;
            resourceInputs["applicationArn"] = undefined /*out*/;
            resourceInputs["grantScope"] = undefined /*out*/;
            resourceInputs["grantee"] = undefined /*out*/;
            resourceInputs["permission"] = undefined /*out*/;
            resourceInputs["s3PrefixType"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["s3PrefixType", "tags[*]"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(AccessGrant.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a AccessGrant resource.
 */
export interface AccessGrantArgs {
    /**
     * The configuration options of the grant location, which is the S3 path to the data to which you are granting access.
     */
    accessGrantsLocationConfiguration?: pulumi.Input<inputs.s3.AccessGrantsLocationConfigurationArgs>;
    /**
     * The custom S3 location to be accessed by the grantee
     */
    accessGrantsLocationId: pulumi.Input<string>;
    /**
     * The ARN of the application grantees will use to access the location
     */
    applicationArn?: pulumi.Input<string>;
    /**
     * The principal who will be granted permission to access S3.
     */
    grantee: pulumi.Input<inputs.s3.AccessGrantGranteeArgs>;
    /**
     * The level of access to be afforded to the grantee
     */
    permission: pulumi.Input<enums.s3.AccessGrantPermission>;
    /**
     * The type of S3SubPrefix.
     */
    s3PrefixType?: pulumi.Input<enums.s3.AccessGrantS3PrefixType>;
    tags?: pulumi.Input<pulumi.Input<inputs.s3.AccessGrantTagArgs>[]>;
}
